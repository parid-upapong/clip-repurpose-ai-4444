# GPU-Optimized ECS Cluster for AI Workers
resource "aws_ecs_cluster" "gpu_cluster" {
  name = "${var.project_name}-gpu-cluster"
}

# Fetch the latest ECS-optimized Amazon Linux 2 AMI for GPU
data "aws_ssm_parameter" "ecs_gpu_ami" {
  name = "/aws/service/ecs/optimized-ami/amazon-linux-2/gpu/recommended/image_id"
}

resource "aws_launch_template" "gpu_worker" {
  name_prefix   = "${var.project_name}-gpu-lt-"
  image_id      = data.aws_ssm_parameter.ecs_gpu_ami.value
  instance_type = var.gpu_instance_type

  iam_instance_profile {
    name = aws_iam_instance_profile.ecs_worker_profile.name
  }

  network_interfaces {
    associate_public_ip_address = true
    security_groups             = [aws_security_group.worker_sg.id]
  }

  # Register the instance to the ECS cluster upon boot
  user_data = base64encode(<<-EOF
              #!/bin/bash
              echo ECS_CLUSTER=${aws_ecs_cluster.gpu_cluster.name} >> /etc/ecs/ecs.config
              EOF
  )
}

resource "aws_autoscaling_group" "gpu_asg" {
  name                = "${var.project_name}-gpu-asg"
  vpc_zone_identifier = [aws_subnet.public.id]
  min_size            = 0
  max_size            = 10
  desired_capacity    = 1

  launch_template {
    id      = aws_launch_template.gpu_worker.id
    version = "$Latest"
  }

  tag {
    key                 = "AmazonECSManaged"
    value               = true
    propagate_at_launch = true
  }
}

# ECS Capacity Provider for Auto-Scaling GPU nodes based on task demand
resource "aws_ecs_capacity_provider" "gpu_cp" {
  name = "${var.project_name}-gpu-cp"

  auto_scaling_group_provider {
    auto_scaling_group_arn = aws_autoscaling_group.gpu_asg.arn
    managed_scaling {
      status                    = "ENABLED"
      target_capacity           = 100
      minimum_scaling_step_size = 1
      maximum_scaling_step_size = 2
    }
  }
}

resource "aws_ecs_cluster_capacity_providers" "gpu_cluster_providers" {
  cluster_name = aws_ecs_cluster.gpu_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.gpu_cp.name]
}

resource "aws_security_group" "worker_sg" {
  name   = "${var.project_name}-worker-sg"
  vpc_id = aws_vpc.main.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
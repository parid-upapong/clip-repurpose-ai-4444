# IAM Role for GPU Worker Instances
resource "aws_iam_role" "ecs_worker_role" {
  name = "${var.project_name}-ecs-worker-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = { Service = "ec2.amazonaws.com" }
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_worker_node_policy" {
  role       = aws_iam_role.ecs_worker_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_iam_role_policy_attachment" "s3_access" {
  role       = aws_iam_role.ecs_worker_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

resource "aws_iam_instance_profile" "ecs_worker_profile" {
  name = "${var.project_name}-worker-profile"
  role = aws_iam_role.ecs_worker_role.name
}
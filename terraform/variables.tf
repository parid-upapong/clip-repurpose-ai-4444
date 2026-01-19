variable "aws_region" {
  description = "AWS region to deploy the infrastructure"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name tag"
  default     = "overlord-ai"
}

variable "gpu_instance_type" {
  description = "EC2 instance type for GPU workers (NVIDIA T4)"
  default     = "g4dn.xlarge"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}
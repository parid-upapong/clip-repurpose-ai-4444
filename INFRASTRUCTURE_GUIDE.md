# Infrastructure Overview: OVERLORD Scalable GPU Cloud

This Terraform configuration sets up a production-ready, auto-scaling GPU processing environment on AWS.

## Architecture Highlights
1.  **Compute:** Amazon ECS Cluster using EC2 `g4dn.xlarge` instances. These instances feature NVIDIA T4 GPUs, ideal for AI inference (Whisper/Face Detection) and FFmpeg hardware acceleration (`h264_nvenc`).
2.  **Orchestration:** ECS Capacity Providers are used to automatically spin up GPU nodes only when there are pending video processing tasks in the queue, minimizing costs.
3.  **Storage:** S3 with lifecycle policies to manage high-volume video data.
4.  **Asynchronous Pipeline:** SQS acts as the buffer. The Backend API (FastAPI) pushes job metadata to SQS, and the Worker Cluster pulls jobs to process.

## Deployment Instructions
1.  Initialize Terraform: `terraform init`
2.  Review Plan: `terraform plan`
3.  Apply: `terraform apply`

## Scaling Strategy
The system scales based on the "Task Demand." When the ECS Service sees more tasks than available GPU nodes can handle, the `gpu_cp` triggers the Auto Scaling Group to launch more G4dn instances.
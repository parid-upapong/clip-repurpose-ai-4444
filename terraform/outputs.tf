output "ecs_cluster_name" {
  value = aws_ecs_cluster.gpu_cluster.name
}

output "sqs_queue_url" {
  value = aws_sqs_queue.video_pipeline_queue.url
}

output "s3_bucket_name" {
  value = aws_s3_bucket.video_assets.id
}

output "gpu_capacity_provider" {
  value = aws_ecs_capacity_provider.gpu_cp.name
}
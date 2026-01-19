# Decoupling Ingestion from GPU Processing
resource "aws_sqs_queue" "video_pipeline_queue" {
  name                      = "${var.project_name}-video-jobs"
  delay_seconds             = 0
  message_retention_seconds = 86400
  receive_wait_time_seconds = 20
  visibility_timeout_seconds = 1800 # 30 mins for heavy video processing

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.video_pipeline_dlq.arn
    maxReceiveCount     = 3
  })
}

resource "aws_sqs_queue" "video_pipeline_dlq" {
  name = "${var.project_name}-video-jobs-dlq"
}
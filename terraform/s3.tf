# Storage for Raw and Processed Video Assets
resource "aws_s3_bucket" "video_assets" {
  bucket = "${var.project_name}-assets-${data.aws_caller_identity.current.account_id}"
}

resource "aws_s3_bucket_lifecycle_configuration" "assets_lifecycle" {
  bucket = aws_s3_bucket.video_assets.id

  rule {
    id     = "cleanup-tmp"
    status = "Enabled"
    filter { prefix = "temp/" }
    expiration { days = 7 }
  }
}

data "aws_caller_identity" "current" {}
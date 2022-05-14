import os
import logging

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

def lambda_handler(event, context):

  # 環境変数取得
  CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
  CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

  line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
  handler = WebhookHandler(CHANNEL_SECRET)

  logger = logging.getLogger()

  # 認証用
  signature = event["headers"]['X-Line-Signature']
  body = event["body"]

  #リターン値の設定
  ok_json = {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {},
    "body": ""
  }
  error_json = {
    "isBase64Encoded": False,
    "statusCode": 500,
    "headers": {},
    "body": "Error"
  }

  @handler.add(MessageEvent, message=TextMessage)
  def message(line_event):
    text = line_event.message.text
    line_bot_api.reply_message(
      line_event.reply_token, TextSendMessage(text=text))

  try:
    handler.handle(body, signature)
  except LineBotApiError as e:
    logger.error("Got exception from LINE Messaging API: %s\n" % e.message)
    for m in e.error.details:
      logger.error("  %s: %s" % (m.property, m.message))

      return error_json

  except InvalidSignatureError:
    logger.error("sending message happen error")

    return error_json

  return ok_json
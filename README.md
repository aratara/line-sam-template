# line-sam-template
AWS SAM Custom Template for LINE Messaging API Echo bot.

## Installation

#### 1. Initialize the project
```
sam init
```  
<br>

**※ Caution**
<br>

Make sure to choose **Custom Template Location** to the first question.  
Then copy and paste the [remote repo link](https://github.com/aratara/line-sam-template.git).
<br>

> Which template source would you like to use?  
> 
>	1 - AWS Quick Start Templates  
>	2 - Custom Template Location  
>	
> Choice: 2
<br>

#### 2. Enter keys for the line messaging api access.

You can create your own line-bot project and corresponding keys from [LINE Developers Console](https://developers.line.biz/console/).  
Both ACCESS_KEY and SECRET_KEY are required to the LINE Messaging API access.  
Copy and paste both of the keys to the vars.json.  
<br>

```
{
  "Parameters": {
    "CHANNEL_ACCESS_TOKEN": "*****",
    "CHANNEL_SECRET": "*****"
  }
}
```

#### 3. Build the project
```
sam build
```

#### 4. Deploy the project
```
sam local start-api --env-vars vars.json
```

## Usage

#### 1. Make http to https
```
ngrok http 3000
```

#### 2. Register https link
Register the https link to [LINE Developers Console](https://developers.line.biz/console/) as **Webhook URL**.  
This will enable us to communicate with the bot.

#### 3. Access from LINE!
Open your LINE App and add this bot. (By the QR code would be fine)  
Chat a message to the bot. You would get the echo message.

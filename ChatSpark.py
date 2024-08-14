from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import os
#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
print(os.environ)
SPARKAI_APP_ID = os.getenv('SPARKAI_APP_ID') 
SPARKAI_API_SECRET =os.getenv('SPARKAI_API_SECRET') 
SPARKAI_API_KEY = os.getenv('SPARKAI_API_KEY')
#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'general'

if __name__ == '__main__':
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content='你好呀'
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    # 假设 a 是一个对象或数据结构
    generations = a.generations  # 获取生成的列表
    # 由于 generations 是一个列表，我们可以访问它的第一个元素
    first_generation = generations[0][0]  # 访问第一个 ChatGeneration 对象
    generated_text = first_generation.text  # 提取生成的文本
    print(generated_text)  # 输出生成的文本


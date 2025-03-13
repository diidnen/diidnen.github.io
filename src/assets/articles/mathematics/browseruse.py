import os
import asyncio
import psutil
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

def kill_edge_processes():
    """关闭所有Edge浏览器进程"""
    for proc in psutil.process_iter(['name']):
        try:
            if 'msedge' in proc.info['name'].lower():
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

async def run_search():
    # 首先清理可能存在的Edge进程
    kill_edge_processes()
    
    # 配置浏览器
    browser_config = BrowserConfig(
        chrome_instance_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        headless=False
    )
    
    browser = None
    try:
        browser = Browser(config=browser_config)
        
        # 设置环境变量
        os.environ['DEEPSEEK_API_KEY'] = 'sk-ecaf12f9541c4eaca2e0cb3ec1621de2'
        
        agent = Agent(
            task=('访问 amazon.com，搜索笔记本电脑，按评分排序，获取第一个结果的价格'),
            llm=ChatOpenAI(
                base_url='https://api.deepseek.com/v1',
                model='deepseek-reasoner',
                api_key='sk-ecaf12f9541c4eaca2e0cb3ec1621de2',
                timeout=30  # 设置API超时
            ),
            browser=browser,
            use_vision=True,  # 启用视觉辅助
            max_failures=3    # 增加容错次数
        )
        
        print("开始执行任务...")
        await agent.run()
        print("任务完成")
    except Exception as e:
        print(f"发生错误: {str(e)}")
    finally:
        if browser:
            print("关闭浏览器...")
            await browser.close()
            print("浏览器已关闭")
        # 再次清理可能残留的Edge进程
        kill_edge_processes()

if __name__ == '__main__':
    print("程序启动...")
    try:
        asyncio.run(run_search())
    finally:
        # 确保程序结束时清理所有Edge进程
        kill_edge_processes()
    print("程序结束")


from locust import HttpUser, task, constant, TaskSet
import logging
 
 
class N11Class(TaskSet):
 
 
    @task
    def get_search_results(self):
            with self.client.get("searchAutoCompleteService?q=telefon&state=f",headers ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"},catch_response=True) as response:
                if(response.status_code == 200) and (response.json()['data']['keywords']['keyword'] is not None):
                    pass
                else:
                    response.failure(response.text)
                    logging.info(response.status_code)
                    logging.info(response.text)
 
 
    @task
    def get_footer_optimization(self):
            with self.client.get("/inventoryName/footer-optimization",headers ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","host":"m.n11.com"},catch_response=True) as response:
                if response.status_code == 200:
                    content = "footer"
                    result = response.search(content,response.text)
                    assert result is not None, "Pattern not found in response text."
                else:
                    response.failure(response.text)
                    logging.info(response.status_code)
                    logging.info(response.text)
 
 
 
def on_start(self):
    print("N11 servisleri çalismaya başladı")
        
    
def on_stop(self):
    print("N11 servisleri bitti")
 
class UserBehavior(HttpUser):
    wait_time = constant(1)
    tasks = [N11Class]
    host = 'https://m.n11.com'
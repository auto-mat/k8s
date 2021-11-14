We have a selenium instance running in the cluster at `selenium-hub.dopracenakole.net`. Login using the format `https://username:password@domain`. The credentials are in `k8s-secrets` on AWS code commit.

**Selenium remote webdriver Python example:**

Check available Selenium Grid node web browser platforms and versions (registered on the Selenium Grid hub):

**Mozilla Firefox**

```
selenium@gnu-linux:~$ curl -H "Accept: application/json" https://username:password@selenium-hub.dopracenakole.net/status | jq '.value.nodes[].slots[].stereotype'

{
  "browserName": "firefox",
  "browserVersion": "94.0",
  "platformName": "Linux",
  "se:vncEnabled": true
}
```

```
selenium@gnu-linux:~$ python
>>> from selenium import webdriver
>>> remote_url = "https://username:password@selenium-hub.dopracenakole.net"
>>> web_page_url = "https://www.dopracenakole.cz/"
>>> firefox_opts = webdriver.FirefoxOptions()
>>> firefox_opts.set_capability("browserVersion", "94.0")
>>> firefox_opts.set_capability("platformName", "Linux")
>>> firefox_drv = webdriver.Remote(command_executor=remote_url, options=firefox_opts)
>>> firefox_drv.get(web_page_url)
>>> "Do práce na kole" in firefox_drv.title
True
>>> firefox_drv.quit()
```

**Google Chrome**

```
selenium@gnu-linux:~$ curl -H "Accept: application/json" https://username:password@selenium-hub.dopracenakole.net/status | jq '.value.nodes[].slots[].stereotype'

{
  "browserName": "chrome",
  "browserVersion": "95.0",
  "platformName": "Linux",
  "se:vncEnabled": true
}
```

```
selenium@gnu-linux:~$ python
>>> from selenium import webdriver
>>> remote_url = "https://username:password@selenium-hub.dopracenakole.net"
>>> web_page_url = "https://www.dopracenakole.cz/"
>>> chrome_opts = webdriver.ChromeOptions()
>>> chrome_opts.set_capability("browserVersion", "95.0")
>>> chrome_opts.set_capability("platformName", "Linux")
>>> chrome_drv = webdriver.Remote(command_executor=remote_url, options=chrome_opts)
>>> chrome_drv.get(web_page_url)
>>> "Do práce na kole" in chrome_drv.title
True
>>> chrome_drv.quit()
```


**Microsoft Edge**

```
selenium@gnu-linux:~$ curl -H "Accept: application/json" https://username:password@selenium-hub.dopracenakole.net/status | jq '.value.nodes[].slots[].stereotype'

{
  "browserName": "MicrosoftEdge",
  "browserVersion": "95.0",
  "platformName": "Linux",
  "se:vncEnabled": true
}
```

```
selenium@gnu-linux:~$ python
>>> from selenium import webdriver
>>> remote_url = "https://username:password@selenium-hub.dopracenakole.net"
>>> web_page_url = "https://www.dopracenakole.cz/"
>>> edge_opts = webdriver.EdgeOptions()
>>> edge_opts.set_capability("browserVersion", "95.0")
>>> edge_opts.set_capability("platformName", "Linux")
>>> edge_drv = webdriver.Remote(command_executor=remote_url, options=edge_opts)
>>> edge_drv.get(web_page_url)
>>> "Do práce na kole" in edge_drv.title
True
>>> edge_drv.quit()
```

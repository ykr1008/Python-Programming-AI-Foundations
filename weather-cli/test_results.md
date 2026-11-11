# Weather CLI - Test Results

| Test | Expected Status / Exception | Actual Result |
|---|---|---|
| Wrong API key | 401 Unauthorized | |
| Nonexistent city | 404 Not Found | |
| Timeout 0.001 | requests.exceptions.Timeout | |
| Valid city | 200 OK | |
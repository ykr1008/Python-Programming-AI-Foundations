# HTTP Concepts – Interview Answers

## 1. Which HTTP methods are safe to retry, and why does it matter?

GET, HEAD, OPTIONS, PUT, and DELETE are generally safe to retry because they are idempotent. This means repeating the same request produces the same final server state as making it once. POST is generally not idempotent because retrying it may create duplicate records or transactions. Understanding this matters when handling network failures because retrying requests incorrectly can cause unintended operations, duplicate data, or payments.

## 2. What is the difference between 401 and 403?

**401 Unauthorized** means valid authentication credentials are missing or not provided, such as an invalid API key. **403 Forbidden** means the server understands the request but refuses access because the authenticated user does not have sufficient permissions. In simple terms, 401 is an authentication problem, while 403 is an authorization problem.

## 3. Why must you always set a timeout?

A timeout specifies how long a program should wait for a server response before stopping the request. Without it, an application may wait indefinitely if the server becomes unresponsive or the network fails. In Python, `requests.get(url, timeout=10)` limits the wait. Timeouts prevent applications from hanging, improve reliability, and allow communication failures to be handled gracefully.

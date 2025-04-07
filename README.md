# xsspayloadgen

**xsspayloadgen** is a simple XSS fuzzer that creates and sends different payloads to test WAFs.

It starts with a few base XSS payloads, applies various mutations to create over 150 unique versions, and sends them to a specified URL and parameter to test the effectiveness of WAFs, input filtering, and XSS protection.

## Mutation Methods

Unicode encoding, HTML entity encoding, Hex encoding, Base64 with eval(atob(...)), breaking up keywords like alert, tweaking event handlers (like onerror), DOM-based script injection.

## How to Use

1. Run the script.
2. Enter the target URL (e.g., `http://example.com/search`).
3. Enter the parameter name (e.g., `q`).
4. It sends all payloads and prints the responses.

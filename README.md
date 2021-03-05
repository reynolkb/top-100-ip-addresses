# Top 100 IP Addresses

## How does your code work?
* The number of requests for each ip address is stored in the ipAddresses dictionary
* The dictionary is sorted by the ip addresses with the top 100 requests

## Why did you choose this approach?
* I chose to use a default dictionary as my approach because it has the fastest run time for managing key data.
* I specified all the values would be integers for a faster run time.

## What other approaches did you decide not to pursue?
* I chose not to optimize the top 100 function because I couldn't figure out how to do it without writing a lot of complicated code.
* For example, I could have had another dictionary only containing the top 100 ip addresses by request.

## What is the runtime complexity of each function?
* requestHandled
    * average - O(1)
    * worst - O(n)
* top100
    * average - O(n log n)
    * worst - O(n log n)
* clear
    * average - O(1)
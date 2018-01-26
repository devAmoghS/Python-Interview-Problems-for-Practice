# Context : The span Si of the stock’s price on a given day i 
# is defined as the maximum number of consecutive days just before
# the given day, for which the price of the stock on the current 
# day is less than or equal to its price on the given day.

# Problem: We have a series of n daily price quotes for a stock 
# and we need to calculate span of stock’s price for all n days

def calculate_span(stock_quotes, span):
  # span for the first quote will always be 1
  span[0] = 1
  for i in range(1, len(stock_quotes), 1):
    # initialize span value to be 1 for each ith quote
    span[i] = 1
    # scan for all the quotes to the left 
    j = i-1
    # if the preceeding quote has a value less than or equal to current quote
    # increase the span value of the current quote
    while(j>=0 and stock_quotes[i]>=stock_quotes[j]):
      span[i] = span[i] + 1
      j = j-1
  return span  
  
quotes = [10, 4, 5, 90, 120, 80]
# initialize span as an empty list with same length as quotes
span_list = [None]*len(quotes)
print(calculate_span(quotes, span_list))
# Result : [1, 1, 2, 4, 5, 1]

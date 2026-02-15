# Fix for search functions

# In search_wikipedia function, change:
# return {"context": [formatted_search_docs]} 
# To:
# return {"context": [formatted_search_docs] if formatted_search_docs else []}

# In search_web function, ensure it returns:
# return {"context": [formatted_search_docs] if formatted_search_docs else []}

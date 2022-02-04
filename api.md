# API Specification
## Overview of app
This backend application is a news service that allows users to follow articles and stories that they're interested in. 

***

## **Gets all articles**
 **GET** /articles/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [ <SERIALIZED COMMENT>, ... ],
         "categories": [ <SERIALIZED CATEGORIES WITHOUT ARTICLE>, ... ],
         "citations": [ <SERIALIZED CITATIONS WITHOUT ARTICLE>, ... ],
         "followers": [ <SERIALIZED FOLLOWERS WITHOUT ARTICLE>, ... ],
         
     }
     ...
 }
```

## **Get a specific article**
 **GET** /articles/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [ <SERIALIZED COMMENT>, ... ],
         "categories": [ <SERIALIZED CATEGORIES WITHOUT ARTICLE>, ... ],
         "citations": [ <SERIALIZED CITATIONS WITHOUT ARTICLE>, ... ],
         "followers": [ <SERIALIZED FOLLOWERS WITHOUT ARTICLE>, ... ],
         
     }
 }
```

## **Create an article**
 **POST** /articles/
 ###### Request
 ```yaml
 {
     "description": <USER INPUT>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [],
         "categories": [],
         "citations": [],
         "followers": [],
         
     }
 }
```

## **Update an article**
 **POST** /articles/{id}/
 ###### Request
```yaml
 {
     "description": <USER INPUT>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [],
         "categories": [],
         "citations": [],
         "followers": [],
         
     }
 }
```

## **Allow user to follow a certain article**
 **POST** /articles/{id}/user/
 ###### Request
```yaml
 {
     "username": <USER INPUT>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [ <SERIALIZED COMMENT>, ... ],
         "categories": [ <SERIALIZED CATEGORIES WITHOUT ARTICLE>, ... ],
         "citations": [ <SERIALIZED CITATIONS WITHOUT ARTICLE>, ... ],
         "followers": [ <SERIALIZED FOLLOWERS WITHOUT ARTICLE>, ... ],
         
     }
 }
```

## **Delete a specific article**
 **DELETE** /articles/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [ <SERIALIZED COMMENT>, ... ],
         "categories": [ <SERIALIZED CATEGORIES WITHOUT ARTICLE>, ... ],
         "citations": [ <SERIALIZED CITATIONS WITHOUT ARTICLE>, ... ],
         "followers": [ <SERIALIZED FOLLOWERS WITHOUT ARTICLE>, ... ],
         
     }
 }
```

***

## **Get all users**
 **GET** /users/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "username": <USER INPUT FOR USERNAME>,
         "following articles": [ <SERIALIZED ARTICLES>, ... ]
     }
 }
```

## **Get a specific user**
 **GET** /users/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "username": <USER INPUT FOR USERNAME>,
         "following articles" : [ <SERIALIZED ARTICLES>, ... ]
     }
 }
```

## **Create a user**
 **POST** /users/
  ###### Request
```yaml
 {
     "username": <USER INPUT FOR NAME>
 }
```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "username": <USER INPUT FOR NAME>,
         "following articles" : []
     }
 }
```

## **Delete a specific user**
 **DELETE** /users/{id}/
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "name": <USER INPUT FOR NAME>,
         "following articles" : [ <SERIALIZED ARTICLES>, ... ]
     }
 }
```
***

## **Get all categories**
 **GET** /categories/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "articles":[ <SERIALIZED ARTICLES>, ... ]
         
     }
     ...
 }
```

## **Get a specific category**
 **GET** /categories/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "articles":[ <SERIALIZED ARTICLES>, ... ]
         
     }
 }
```

## **Delete a specific category**
 **DEL** /categories/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "articles":[ <SERIALIZED ARTICLES>, ... ]
         
     }
 }
```

## **Pair an article with a category**
 **POST** /articles/{id}/category/
 ###### Request
```yaml
 {
     "description": <USER INPUT>
 }
```
###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "comments": [ <SERIALIZED COMMENT>, ... ],
         "categories": [ <SERIALIZED CATEGORIES WITHOUT ARTICLE>, ... ],
         "citations": [ <SERIALIZED CITATIONS WITHOUT ARTICLE>, ... ],
         "followers": [ <SERIALIZED FOLLOWERS WITHOUT ARTICLE>, ... ]
         
     }
 }
```

## **Get all citations**
 **GET** /citations/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "title": <USER INPUT FOR TITLE>,
         "author": <USER INPUT FOR AUTHOR>,
         "articles": [ <SERIALIZED ARTICLES>, ... ]
     }
     ...
 }
```

## **Get a specific citation**
 **GET** /citations/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "title": <USER INPUT FOR TITLE>,
         "author": <USER INPUT FOR AUTHOR>,
         "articles": [ <SERIALIZED ARTICLES>, ... ]
     }
 }
```

## **Delete a specific citation**
 **DEL** /citations/{id}/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "title": <USER INPUT FOR TITLE>,
         "author": <USER INPUT FOR AUTHOR>,
         "articles": [ <SERIALIZED ARTICLES>, ... ]
     }
 }
```

## **Assign a citation to an article**
 **POST** /articles/{id}/cite/
 ###### Request
 ```yaml
 {
     "author": <USER INPUT FOR AUTHOR>
     "title": <USER INPUT FOR TITLE
 }
 ```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "title": <USER INPUT FOR TITLE>,
         "author": <USER INPUT FOR AUTHOR>,
         "articles": [ <SERIALIZED ARTICLES>, ... ]
     }
 }
```

## **Get all comments on an article**
 **GET** /articles/{id}/comments/
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "article_id":[ <STORED ID FOR ARTICLE WITH ID {id}>, ... ]
         
     }
     ...
 }
```

## **Create a comment on an article**
 **POST** /articles/{id}/comments/
  ###### Request
  ```yaml
 {
     "description": <USER INPUT>
 }
 ```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "article_id":[ <STORED ID FOR ARTICLE WITH ID {id2}>, ... ]
         
     }
 }
```

## **Delete a comment**
 **DEL** /articles/{id1}/comments/{id2]
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "article_id":[ <STORED ID FOR ARTICLE WITH ID {id1}>, ... ]
         
     }
     ...
 }
```

## **Update a comment on an article**
 **POST** /articles/{id}/comments/
  ###### Request
  ```yaml
 {
     "description": <USER INPUT>
 }
 ```
 ###### Response
 ```yaml
 {
     "success": true,
     "data": {
         "id": <ID>,
         "description": <USER INPUT FOR DESCRIPTION>,
         "article_id":[ <STORED ID FOR ARTICLE WITH ID {id2}>, ... ]
         
     }
 }
```




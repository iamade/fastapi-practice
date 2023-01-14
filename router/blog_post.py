from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Dict, Optional, List
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str 
    nb_comment: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None 

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version':version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, comment_title: int = Query(None,
                title='Title of the comment',
                description='Some description for comment_title',
                alias='commentTitle',
                deprecated=True 
                ),
                content: str = Body(..., min_length=10, max_length=12, regex='^[a-z\s]$'),
                v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
                comment_id: int = Path(None, gt=5, le =10)
                # content: str = Body('hi how are you')
                ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'return': v,
        'comment_id': comment_id
    }

def required_functionality():
    return {'message': 'Learning FastAPI is important'}
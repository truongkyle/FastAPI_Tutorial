from datetime import datetime
import uuid
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
from app.oauth2 import require_user

router = APIRouter()

@router.get('/{post_id}')
def get_single_post(post_id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    post_data = db.query(models.Post).filter(models.Post.id == uuid.UUID(post_id)).first()
    
    if not post_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="post don't exists")
    if post_data.user_id != uuid.UUID(user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you don't have permission to update this post")

    return{"status": "success", "data": post_data}

@router.get('/{skip}/{limit}')
def get_posts(skip: int = 0, limit: int =10, db : Session = Depends(get_db), user_id: str = Depends(require_user)):
    posts = db.query(models.Post).filter(models.Post.user_id == user_id).limit(limit).offset(skip).all()
    return {'status':"success", 'results': len(posts), 'posts': posts}

@router.post('/')
def create_post(payload: schemas.CreatePostSchema, db : Session = Depends(get_db), user_id : str = Depends(require_user)):
    payload.user_id = uuid.UUID(user_id)
    new_post =models.Post(**payload.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post    

@router.put('/{post_id}')
def update_post(post_id: str, payload: schemas.CreatePostSchema, db: Session = Depends(get_db), user_id : str = Depends(require_user)):
    post_query = db.query(models.Post).filter(models.Post.id == uuid.UUID(post_id))
    post_data = post_query.first()

    if not post_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="post don't exists")
    if post_data.user_id != uuid.UUID(user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you don't have permission to update this post")
    
    payload.user_id = uuid.UUID(user_id)

    post_query.update(payload.dict(exclude_unset=True), synchronize_session=False)
    db.commit()

    return payload

@router.delete('/{post_id}')
def delete_post(post_id: str, db: Session = Depends(get_db), user_id = Depends(require_user)):
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post_data = post_query.first()

    if not post_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="post don't exists")

    if post_data.user_id != uuid.UUID(user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you are not allowed to perform this action")
    
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
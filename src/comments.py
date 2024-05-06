from flask import Blueprint, request, jsonify
from .models import db, Comment

comments_bp = Blueprint('comments', __name__)

# Create a new comment 
@comments_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    content = data.get('content')
    post_id = data.get('post_id')
    author_id = data.get('author_id')

    if not content or not post_id or not author_id:
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_comment = Comment(content=content, post_id=post_id, author_id=author_id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify(new_comment.serialize()), 201

# get all comments 
@comments_bp.route('', methods=['GET'])
def list_comments():
    comments = Comment.query.all()
    serialized_comments = [comment.serialize() for comment in comments]
    return jsonify(serialized_comments), 200

# updating comments by ID
@comments_bp.route('<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    data = request.get_json()

    if 'content' in data:
        comment.content = data['content']

    db.session.commit()
    return jsonify(comment.serialize()), 200

# Delete a comment by ID 
@comments_bp.route('<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment successfully deleted!'})
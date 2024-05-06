from flask import Blueprint, request, jsonify
from .models import db, Post

posts_bp = Blueprint('posts', __name__)

# To create a new post
@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    category_id = data.get('category_id')
    author_id = data.get('author_id')

    if not title or not content or not category_id or not author_id:
        return jsonify({'error': 'Missing required fields'}), 400

    new_post = Post(title=title, content=content, category_id=category_id, author_id=author_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.serialize()), 201

# would need to get a list of all the post if ever needed for user and admin use
@posts_bp.route('', methods=['GET'])
def list_posts():
    posts = Post.query.all()
    serialized_posts = [post.serialize() for post in posts]
    return jsonify(serialized_posts), 200

# Updating a post by ID for user and admin use
@posts_bp.route('<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()

    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    if 'category_id' in data:
        post.category_id = data['category_id']
    if 'author_id' in data:
        post.author_id = data['author_id']

    db.session.commit()
    return jsonify(post.serialize()), 200

# To delete a post I'm wondering if i just try and make it admin use or give users access?
@posts_bp.route('<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post has been successfully deleted!'}), 200
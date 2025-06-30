from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models import db, Appearance, Guest, Episode

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    if not all(key in data for key in ['rating', 'guest_id', 'episode_id']):
        return jsonify({"error": "rating, guest_id, and episode_id are required"}), 400
    
    if not 1 <= data['rating'] <= 5:
        return jsonify({"error": "Rating must be between 1 and 5"}), 400
    
    if not Guest.query.get(data['guest_id']):
        return jsonify({"error": "Guest not found"}), 404
    
    if not Episode.query.get(data['episode_id']):
        return jsonify({"error": "Episode not found"}), 404
    
    appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201
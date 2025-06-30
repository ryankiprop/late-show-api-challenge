from .models import db, User, Guest, Episode, Appearance
from .app import create_app
from datetime import date

app = create_app()

def seed_data():
    with app.app_context():
        
        db.session.query(Appearance).delete()
        db.session.query(Guest).delete()
        db.session.query(Episode).delete()
        db.session.query(User).delete()
        db.session.commit()
        
        
        user = User(username='testuser')
        user.set_password('testpass')
        db.session.add(user)
        
        
        guests = [
            Guest(name='John Doe', occupation='Actor'),
            Guest(name='Jane Smith', occupation='Musician'),
            Guest(name='Bob Johnson', occupation='Comedian')
        ]
        db.session.add_all(guests)
        
        
        episodes = [
            Episode(date=date(2023, 1, 1), number=101),
            Episode(date=date(2023, 1, 2), number=102),
            Episode(date=date(2023, 1, 3), number=103)
        ]
        db.session.add_all(episodes)
        
        db.session.commit()
        
        
        appearances = [
            Appearance(rating=4, guest_id=1, episode_id=1),
            Appearance(rating=5, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2),
            Appearance(rating=5, guest_id=1, episode_id=3)
        ]
        db.session.add_all(appearances)
        
        db.session.commit()
        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
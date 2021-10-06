from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False) 
    birth_year =  db.Column(db.String(250), unique=True, nullable=False) 
    eye_color = db.Column(db.String(250), unique=True, nullable=False) 
    gender = db.Column(db.String(250), unique=True, nullable=False) 
    hair_color = db.Column(db.String(250), unique=True, nullable=False) 
    height = db.Column(db.String(250), unique=True, nullable=False) 
    mass = db.Column(db.String(250), unique=True, nullable=False) 
    skin_color = db.Column(db.String(250), unique=True, nullable=False) 
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    homeworld = db.relationship("Planet")
    url = db.Column(db.String(250), unique=True, nullable=False) 
    created = db.Column(db.String(250), unique=True, nullable=False) 
    edited = db.Column(db.String(250), unique=True, nullable=False) 

    def __repr__(self):
        return f'<People {self.name}-{self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "url": self.url,
            "created": self.created,
            "edited": self.edited
            
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(250), unique=True, nullable=False) 
    diameter = db.Column(db.String(250), unique=True, nullable=False) 
    rotation_period = db.Column(db.String(250), unique=True, nullable=False) 
    orbital_period = db.Column(db.String(250), unique=True, nullable=False) 
    gravity = db.Column(db.String(250), unique=True, nullable=False) 
    population = db.Column(db.String(250), unique=True, nullable=False) 
    climate = db.Column(db.String(250), unique=True, nullable=False) 
    terrain = db.Column(db.String(250), unique=True, nullable=False) 
    surface_water = db.Column(db.String(250), unique=True, nullable=False) 
    url = db.Column(db.String(250), unique=True, nullable=False) 

    def __repr__(self):
        return f'<Planet {self.name}-{self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter" : self.diameter, 
            "rotation_period" : self.rotation_period, 
            "orbital_period" : self.orbital_period, 
            "gravity" : self.gravity,
            "population" : self.population, 
            "climate" : self.climate,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water,
            "url" : self.url
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    model = db.Column(db.String(250), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(250), unique=True, nullable=False)
    manufacturer = db.Column(db.String(250), unique=True, nullable=False)
    length = db.Column(db.String(250), unique=True, nullable=False)
    cost_in_credits = db.Column(db.String(250), unique=True, nullable=False) 
    crew = db.Column(db.String(250), unique=True, nullable=False) 
    passengers = db.Column(db.String(250), unique=True, nullable=False) 
    max_atmosphering_speed = db.Column(db.String(250), unique=True, nullable=False) 
    cargo_capacity = db.Column(db.String(250), unique=True, nullable=False) 
    consumables = db.Column(db.String(250), unique=True, nullable=False) 
    url = db.Column(db.String(250), unique=True, nullable=False) 
    created = db.Column(db.String(250), unique=True, nullable=False) 
    edited = db.Column(db.String(250), unique=True, nullable=False) 

    def __repr__(self):
        return f'<Vehicle {self.name}-{self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model" : self.model,
            "vehicle_class" : self.vehicle_class,
            "manufacturer" : self.manufacturer,
            "length" : self.length,
            "cost_in_credits" : self.cost_in_credits, 
            "crew" : self.crew,
            "passengers" : self.passengers, 
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "cargo_capacity" : self.cargo_capacity,
            "consumables" : self.consumables, 
            "url" : self.url,
            "created" : self.created, 
            "edited" : self.edited
        }

class UserPeopleFavorites(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user = db.relationship("User")
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"), primary_key=True)
    people = db.relationship("People")

class UserPlanetsFavorites(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user = db.relationship("User")
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), primary_key=True)
    planet = db.relationship("Planet")

class UserVehiclesFavorites(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user = db.relationship("User")
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), primary_key=True)
    vehicle = db.relationship("Vehicle")
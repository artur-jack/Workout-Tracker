from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu_secret_key_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'
db = SQLAlchemy(app)

class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    exercises = db.relationship("Exercise", back_populates="workout", cascade="all, delete-orphan")

class Exercise(db.Model):
    __tablename__ = 'exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    name = db.Column(db.String, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    current_weight = db.Column(db.Float)
    pr_weight = db.Column(db.Float)
    workout = db.relationship("Workout", back_populates="exercises")

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    workouts = Workout.query.all()
    return render_template('index.html', workouts=workouts)

@app.route('/workout/add', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        day = request.form['day']
        name = request.form['name']
        
        workout = Workout(day_of_week=day, name=name)
        db.session.add(workout)
        
        exercise_names = request.form.getlist('exercise_name[]')
        sets = request.form.getlist('sets[]')
        reps = request.form.getlist('reps[]')
        current_weights = request.form.getlist('current_weight[]')
        pr_weights = request.form.getlist('pr_weight[]')
        
        for i in range(len(exercise_names)):
            if exercise_names[i]:
                exercise = Exercise(
                    name=exercise_names[i],
                    sets=int(sets[i]),
                    reps=int(reps[i]),
                    current_weight=float(current_weights[i]) if current_weights[i] else None,
                    pr_weight=float(pr_weights[i]) if pr_weights[i] else None
                )
                workout.exercises.append(exercise)
        
        db.session.commit()
        flash('Treino adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_workout.html', workout=None)

@app.route('/workout/edit/<int:workout_id>', methods=['GET', 'POST'])
def edit_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    
    if request.method == 'POST':
        workout.day_of_week = request.form['day']
        workout.name = request.form['name']
        
        # Remove existing exercises
        workout.exercises = []
        
        exercise_names = request.form.getlist('exercise_name[]')
        sets = request.form.getlist('sets[]')
        reps = request.form.getlist('reps[]')
        current_weights = request.form.getlist('current_weight[]')
        pr_weights = request.form.getlist('pr_weight[]')
        
        for i in range(len(exercise_names)):
            if exercise_names[i]:
                exercise = Exercise(
                    name=exercise_names[i],
                    sets=int(sets[i]),
                    reps=int(reps[i]),
                    current_weight=float(current_weights[i]) if current_weights[i] else None,
                    pr_weight=float(pr_weights[i]) if pr_weights[i] else None
                )
                workout.exercises.append(exercise)
        
        db.session.commit()
        flash('Treino atualizado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_workout.html', workout=workout)

@app.route('/workout/delete/<int:workout_id>')
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Treino excluído com sucesso!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

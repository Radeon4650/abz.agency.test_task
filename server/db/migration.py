from server import app, engine
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, engine)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
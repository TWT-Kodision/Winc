# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting = 'Hello, <name>!'):
    new_greeting = greeting.replace('<name>', name)
    return (new_greeting)
    
def force(mass, body = 'earth'):
    body = body.lower()
    gravitys = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'veus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }
    body_force = mass * gravitys[body]
    return body_force

def pull(m1, m2, d):
    G = 6.674*10**-11
    gravitational_pull =  G*(m1*m2)/d**2
    return gravitational_pull
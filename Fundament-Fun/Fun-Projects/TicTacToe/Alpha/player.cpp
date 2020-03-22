Player::Player (string name, int id, int points) {
  this->name   = name;
  this->id     = id;
  this->points = points;
}

Player::Player (const Player& input) {
  name   = input.Name();
  id     = input.ID();
  points = input.Points();
}

Player& Player::operator = (const Player& input) {
  if (this != &input) {
    name   = input.Name();
    id     = input.ID();
    points = input.Points();
  }

  return *this;
}

Player::~Player () { ; }

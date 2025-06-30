-- This SQL script creates the necessary tables for the application.
-- MikoBot (c) 2024-2025 by Void

-- USERS TABLE
-- This table is used to store user information.
-- The created column is used to store the timestamp when the user was created.
-- The username column is used to store the user's name.
-- The email column is used to store the user's email address.
-- The password column is used to store the user's password.
-- The permissions column is used to store the user's permissions (e.g., admin, user).
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  username TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  permissions TEXT NOT NULL DEFAULT 'user'
);

-- TOKENS TABLE
-- This table is used to store tokens for various purposes.
-- The purpose column is used to identify the purpose of the token.
-- The token column is used to store the actual token value.
CREATE TABLE IF NOT EXISTS tokens (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  purpose TEXT NOT NULL,
  token TEXT NOT NULL
);

-- EMAIL_PROVIDERS TABLE
-- This table is used to store email provider configurations.
-- The created column is used to store the timestamp when the provider was created.
-- The name column is used to store the name of the email provider.
-- The host column is used to store the SMTP host of the email provider.
-- The port column is used to store the SMTP port of the email provider.
-- The username column is used to store the username for the email provider.
-- The password column is used to store the password for the email provider.
-- The use_ssl column is used to indicate whether SSL should be used for the connection.
CREATE TABLE IF NOT EXISTS email_providers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT NOT NULL,
  host TEXT NOT NULL,
  port INTEGER NOT NULL,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  use_ssl BOOLEAN NOT NULL DEFAULT TRUE
);

-- EMAIL_TEMPLATES TABLE
-- This table is used to store email templates.
-- The created column is used to store the timestamp when the template was created.
-- The name column is used to store the name of the template.
-- The subject column is used to store the subject of the email.
-- The body column is used to store the body of the email.
CREATE TABLE IF NOT EXISTS email_templates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT NOT NULL,
  subject TEXT NOT NULL,
  body TEXT NOT NULL
);

-- LOGS TABLE
-- This table is used to store logs for various events.
-- The created column is used to store the timestamp when the log was created.
-- The type column is used to identify the type of log (e.g., error, info).
-- The message column is used to store the actual log message.
CREATE TABLE IF NOT EXISTS logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  type TEXT NOT NULL,
  message TEXT NOT NULL
);

-- GAMES TABLE
-- This table is used to store game information.
-- The created column is used to store the timestamp when the game was created.
-- The keyname column is used to store a unique key for the game.
-- The name column is used to store the name of the game.
-- The image column is used to store the URL of the game's image.
CREATE TABLE IF NOT EXISTS games (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  keyname TEXT NOT NULL,
  name TEXT NOT NULL,
  image TEXT NOT NULL
);
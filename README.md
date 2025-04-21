# Odoo Development Environment Setup

This project provides a Docker-based development environment for Odoo Community Edition, including PostgreSQL database and custom addons support.

## Prerequisites

- Docker and Docker Compose installed
- Git (optional, for version control)
- Basic understanding of Linux commands

## Project Structure

```
.
├── docker-compose.yml      # Docker Compose configuration
├── config/
│   └── odoo.conf          # Odoo configuration file
├── addons/
│   └── custom_module/     # Sample custom module
└── README.md              # This documentation
```

## Setup Instructions

1. Clone this repository (if using Git)
2. Create the necessary directories:
   ```bash
   mkdir -p config addons
   ```

3. Start the containers:
   ```bash
   docker-compose up -d
   ```

4. Access Odoo:
   - Open your browser and go to: `http://localhost:8069`
   - Default credentials:
     - Database: `odoo`
     - Username: `admin`
     - Password: `admin`

## Debug Mode

To enable debug mode:
1. Access Odoo with `?debug=1` parameter: `http://localhost:8069?debug=1`
2. This will show:
   - Technical features menu
   - View inheritance information
   - Field attributes
   - Debug assets

## Logging Configuration

The environment is configured with detailed logging:
- Log level: DEBUG
- Logs are stored in both file and database
- Sample log entries can be found in the custom module's `res_partner.py`

## Odoo Architecture Overview

### Core Components

1. **Backend**
   - Python-based server
   - ORM (Object-Relational Mapping)
   - Security and access control
   - Business logic

2. **Frontend**
   - Web client
   - QWeb template engine
   - JavaScript framework
   - Responsive design

3. **Database**
   - PostgreSQL
   - Automatic schema management
   - Data integrity
   - Transaction support

4. **ORM Features**
   - Automatic CRUD operations
   - Inheritance mechanisms
   - Computed fields
   - Constraints and validations

## Debug Tools

1. **Technical Features**
   - Access via debug mode
   - View technical menus
   - Inspect models and fields

2. **Logging**
   - Configured in `odoo.conf`
   - Multiple log handlers
   - Database logging enabled

3. **Developer Tools**
   - View inheritance
   - Field attributes
   - Debug assets
   - Technical menus

## Troubleshooting

1. **Container Issues**
   ```bash
   docker-compose logs -f web  # View Odoo logs
   docker-compose logs -f db   # View PostgreSQL logs
   ```

2. **Database Issues**
   - Check PostgreSQL connection
   - Verify database credentials
   - Ensure proper volume mounting

3. **Addons Issues**
   - Verify addons path
   - Check module dependencies
   - Review module manifest

## Best Practices

1. Always use debug mode during development
2. Monitor logs for errors and warnings
3. Use version control for custom modules
4. Regular database backups
5. Test in isolated environments

## Security Notes

- Change default passwords
- Use secure database credentials
- Implement proper access controls
- Regular security updates 
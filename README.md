# PropertyPulse: Streamlining Rental Management

## Introduction
PropertyPulse is designed to revolutionize the rental management process by providing a streamlined, efficient, and user-friendly platform for landlords, property managers, and tenants. By leveraging modern technologies, PropertyPulse aims to address inefficiencies in traditional property management processes, including cumbersome paperwork, manual data entry, and fragmented communication channels.

**Deployed Site**: [PropertyPulse](#)  
**Final Project Blog Article**: [Read Here](#)  
**Authors**:
- Solomon Kaniaru [LinkedIn](#)
- Mercy Waweru [LinkedIn](#)

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/20407002036/propertypulse.git
    cd propertypulse
    ```

2. **Backend Setup**:
    - Ensure you have Python and Node.js installed.
    - Install backend dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    - Set up environment variables:
        ```bash
        cp .env.example .env
        ```
        Modify the `.env` file with your database credentials and other configurations.
    - Initialize the database:
        ```bash
        flask db init
        flask db migrate
        flask db upgrade
        ```

3. **Frontend Setup**:
    - Navigate to the frontend directory and install dependencies:
        ```bash
        cd client
        npm install
        ```

4. **Run the Application**:
    - Start the backend server:
        ```bash
        flask run
        ```
    - Start the frontend development server:
        ```bash
        cd client
        npm start
        ```

## Usage
Once the application is up and running, you can access the platform at `http://localhost:3000`. The platform provides various features for different user roles:

- **Landlords/Property Managers**:
  - Manage leases
  - Handle tenant communications
  - Track maintenance requests
  - Process financial transactions

- **Tenants**:
  - Streamlined communication channels
  - Online rent payments
  - Maintenance request tracking

## Contributing
We welcome contributions from the community! To contribute to PropertyPulse, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows our coding guidelines and includes appropriate tests.

## Related Projects
Here are some related projects and tools that might interest you:
- [Buildium](https://www.buildium.com)
- [AppFolio](https://www.appfolio.com)
- [RentManager](https://www.rentmanager.com)
- [Cozy](https://www.cozy.co)
- [Stessa](https://www.stessa.com)
- [OpenMAINT](https://www.openmaint.org)

## Licensing
PropertyPulse is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
**Solomon Kaniaru & Mercy Waweru**  
PropertyPulse Development Team

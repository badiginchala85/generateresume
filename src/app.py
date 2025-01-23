from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Resume", 0, 1, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set the title and add content
pdf.set_font("Arial", size=12)

# Add Contact Information
pdf.cell(0, 10, "Your Name", 0, 1, "C")
pdf.cell(0, 10, "Contact Information:", 0, 1, "L")
pdf.cell(0, 10, "Email: Your Email Address", 0, 1, "L")
pdf.cell(0, 10, "Phone: Your Phone Number", 0, 1, "L")
pdf.cell(0, 10, "LinkedIn: Your LinkedIn Profile", 0, 1, "L")
pdf.cell(0, 10, "GitHub: Your GitHub Profile", 0, 1, "L")

# Add Summary
pdf.chapter_title("Summary:")
summary_text = (
    "Enthusiastic and detail-oriented DevOps Engineer with over [X] years of experience in managing "
    "cloud infrastructure, deploying and orchestrating containerized applications, and automating "
    "CI/CD pipelines. Skilled in Azure DevOps, Docker, Kubernetes, AWS, and monitoring tools to "
    "ensure the reliability and scalability of applications. Adept at collaborating with cross-functional "
    "teams to optimize workflows and improve system performance."
)
pdf.chapter_body(summary_text)

# Add Technical Skills
pdf.chapter_title("Technical Skills:")
skills_text = (
    "DevOps Tools: Azure DevOps, Jenkins, Git, GitHub, GitLab CI/CD\n"
    "Containerization & Orchestration: Docker, Docker Compose, Kubernetes\n"
    "Cloud Platforms: AWS (EC2, S3, RDS, Lambda, CloudFormation), Azure\n"
    "Infrastructure as Code (IaC): Terraform, Ansible, AWS CloudFormation\n"
    "Monitoring & Logging: Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), AWS CloudWatch\n"
    "Configuration Management: Ansible, Chef, Puppet\n"
    "Programming Languages: Python, Bash, PowerShell\n"
    "Operating Systems: Linux (Ubuntu, CentOS), Windows"
)
pdf.chapter_body(skills_text)

# Add Professional Experience
pdf.chapter_title("Professional Experience:")
experience_text = (
    "DevOps Engineer\n"
    "Company Name - Location\n"
    "Month, Year - Present\n"
    "- Designed and implemented CI/CD pipelines using Azure DevOps, resulting in a [X]% reduction in deployment time.\n"
    "- Containerized applications using Docker and orchestrated them with Kubernetes, enhancing scalability and resilience.\n"
    "- Managed AWS infrastructure, including EC2 instances, S3 buckets, RDS databases, and Lambda functions.\n"
    "- Automated infrastructure provisioning with Terraform, reducing manual intervention and minimizing configuration drift.\n"
    "- Set up monitoring and logging solutions using Prometheus, Grafana, and ELK Stack to ensure system reliability and performance.\n"
    "- Collaborated with development and operations teams to improve deployment processes and system stability.\n"
    "- Conducted performance tuning, troubleshooting, and capacity planning to optimize resource utilization.\n"
    "\n"
    "Systems Administrator\n"
    "Previous Company Name - Location\n"
    "Month, Year - Month, Year\n"
    "- Administered and maintained server environments, ensuring high availability and performance.\n"
    "- Implemented configuration management solutions using Ansible and Puppet to automate repetitive tasks.\n"
    "- Managed version control systems (Git, GitHub) and supported development teams with branching and merging strategies.\n"
    "- Developed scripts in Python and Bash to automate routine tasks and improve efficiency.\n"
    "- Monitored system performance and resolved issues using AWS CloudWatch and custom monitoring solutions.\n"
    "- Conducted regular security assessments and implemented best practices to secure infrastructure."
)
pdf.chapter_body(experience_text)

# Add Education
pdf.chapter_title("Education:")
education_text = (
    "Bachelor of Science in Computer Science\n"
    "University Name - Location\n"
    "Year of Graduation"
)
pdf.chapter_body(education_text)

# Add Certifications
pdf.chapter_title("Certifications:")
certifications_text = (
    "AWS Certified Solutions Architect - Associate\n"
    "Certified Kubernetes Administrator (CKA)\n"
    "Microsoft Certified: Azure DevOps Engineer Expert\n"
    "Docker Certified Associate (DCA)"
)
pdf.chapter_body(certifications_text)

# Add Projects
pdf.chapter_title("Projects:")
projects_text = (
    "Automated Deployment Pipeline\n"
    "- Developed and deployed an automated CI/CD pipeline using Azure DevOps, Docker, and Kubernetes for a microservices-based application.\n"
    "- Configured monitoring and alerting with Prometheus and Grafana to track application performance and health.\n"
    "\n"
    "Infrastructure as Code (IaC) Implementation\n"
    "- Implemented IaC using Terraform for AWS resources, including EC2, VPC, S3, and RDS.\n"
    "- Automated configuration management with Ansible to ensure consistent and repeatable deployments."
)
pdf.chapter_body(projects_text)

# Add Soft Skills
pdf.chapter_title("Soft Skills:")
soft_skills_text = (
    "Strong communication and collaboration skills\n"
    "Problem-solving and analytical thinking\n"
    "Adaptable and quick learner\n"
    "Attention to detail and reliability"
)
pdf.chapter_body(soft_skills_text)

# Save the PDF to a file
pdf.output("Resume.pdf")

print("PDF generated successfully.")

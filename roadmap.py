def generate_roadmap(goal):
    roadmaps = {
        "Web Development": [
            "Learn HTML, CSS, JavaScript",
            "Learn Responsive Design",
            "Learn Git & GitHub",
            "Learn React.js",
            "Learn Backend Development with FastAPI or Node.js",
            "Build Full Stack Projects",
            "Deploy Projects Online"
        ],
        "AI / ML": [
            "Learn Python Basics",
            "Learn NumPy and Pandas",
            "Learn Data Visualization",
            "Learn Machine Learning",
            "Build ML Projects",
            "Learn Deep Learning",
            "Explore AI Tools and APIs"
        ],
        "Data Science": [
            "Learn Python for Data Analysis",
            "Learn Pandas & NumPy",
            "Learn Data Cleaning",
            "Learn Data Visualization",
            "Learn Machine Learning",
            "Work on Real-world Datasets",
            "Build Data Science Projects"
        ],
        "Cybersecurity": [
            "Learn Networking Basics",
            "Learn Linux Fundamentals",
            "Understand Cybersecurity Concepts",
            "Learn Ethical Hacking",
            "Practice on TryHackMe or Hack The Box",
            "Learn Web Security",
            "Prepare for Security Certifications"
        ],
        "Cloud Computing": [
            "Learn Linux Basics",
            "Understand Cloud Concepts",
            "Learn AWS Fundamentals",
            "Learn Docker",
            "Learn Kubernetes",
            "Deploy Applications on Cloud",
            "Learn DevOps Basics"
        ],
        "Mobile App Development": [
            "Learn Programming Basics",
            "Learn Flutter or React Native",
            "Build Mobile UI",
            "Connect APIs",
            "Build Android/iOS Apps",
            "Publish Apps",
            "Create Portfolio Apps"
        ],
        "UI/UX Design": [
            "Learn Design Principles",
            "Learn Figma",
            "Understand Color Theory",
            "Create Wireframes",
            "Design Mobile & Web Interfaces",
            "Build UI/UX Portfolio",
            "Learn User Research"
        ],
        "DevOps": [
            "Learn Linux",
            "Learn Git & GitHub",
            "Understand CI/CD",
            "Learn Docker",
            "Learn Kubernetes",
            "Learn Jenkins",
            "Deploy Projects"
        ],
        "Blockchain": [
            "Learn Blockchain Basics",
            "Understand Cryptocurrency",
            "Learn Solidity",
            "Build Smart Contracts",
            "Learn Web3",
            "Build Blockchain Projects",
            "Explore Decentralized Apps"
        ],
        "Job Preparation": [
            "Practice DSA Daily",
            "Learn Aptitude",
            "Prepare Resume",
            "Practice Mock Interviews",
            "Build Projects",
            "Improve Communication Skills",
            "Apply for Internships"
        ],
        "General Growth": [
            "Improve Communication Skills",
            "Practice Coding Daily",
            "Build Small Projects",
            "Read Technical Blogs",
            "Learn Git & GitHub",
            "Improve LinkedIn Profile",
            "Participate in Hackathons"
        ]
    }

    return roadmaps.get(goal, [
        "Learn DSA",
        "Practice Coding",
        "Build Projects",
        "Prepare Resume",
        "Interview Preparation"
    ])

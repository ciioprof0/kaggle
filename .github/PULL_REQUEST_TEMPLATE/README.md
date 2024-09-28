In a GitHub repository, the `.github/PULL_REQUEST_TEMPLATE/` directory is used to store pull request (PR) templates. These templates help standardize the information contributors provide when submitting pull requests, ensuring that all necessary details are included for reviewers to understand and assess the changes effectively.

## **Common Files in `.github/PULL_REQUEST_TEMPLATE/`**

1. **`pull_request_template.md`**

   - **Description:**
     The primary template that is used by default when a contributor opens a new pull request. This single template serves as a standardized format for all PR submissions unless multiple templates are defined.

   - **Example Content:**
     ```markdown
     ## Description

     Please include a summary of the changes and the related issue. Please also include relevant motivation and context. List any dependencies that are required for this change.

     Fixes #(issue)

     ## Type of Change

     Please delete options that are not relevant.

     - [ ] Bug fix (non-breaking change which fixes an issue)
     - [ ] New feature (non-breaking change which adds functionality)
     - [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
     - [ ] Documentation Update

     ## How Has This Been Tested?

     Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce. Please also list any relevant details for your test configuration

     - [ ] Test A
     - [ ] Test B

     ## Checklist:

     - [ ] My code follows the style guidelines of this project
     - [ ] I have performed a self-review of my own code
     - [ ] I have commented my code, particularly in hard-to-understand areas
     - [ ] I have made corresponding changes to the documentation
     - [ ] My changes generate no new warnings
     - [ ] I have added tests that prove my fix is effective or that my feature works
     - [ ] New and existing unit tests pass locally with my changes
     - [ ] Any dependent changes have been merged and published in downstream modules
     ```

2. **Multiple Pull Request Templates**

   - **Description:**
     When a repository has diverse types of pull requests (e.g., features, bug fixes, documentation updates), multiple templates can be created to cater to each type. Each template should be placed in the `.github/PULL_REQUEST_TEMPLATE/` directory with a descriptive name.

   - **Naming Convention:**
     The filenames should clearly indicate the purpose of each template. GitHub uses the template name to allow contributors to select the appropriate one when opening a PR.

   - **Example Files:**
     - `feature_template.md`
     - `bugfix_template.md`
     - `documentation_template.md`

   - **Example Content for `feature_template.md`:**
     ```markdown
     ## 🚀 Feature Proposal

     **Is your feature request related to a problem? Please describe.**

     A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

     **Describe the solution you'd like**

     A clear and concise description of what you want to happen.

     **Additional context**

     Add any other context or screenshots about the feature request here.
     ```

   - **Example Content for `bugfix_template.md`:**
     ```markdown
     ## 🐛 Bug Report

     **Describe the bug**

     A clear and concise description of what the bug is.

     **To Reproduce**

     Steps to reproduce the behavior:
     1. Go to '...'
     2. Click on '....'
     3. Scroll down to '....'
     4. See error

     **Expected behavior**

     A clear and concise description of what you expected to happen.

     **Screenshots**

     If applicable, add screenshots to help explain your problem.

     **Environment:**
     - OS: [e.g., Windows, macOS, Linux]
     - Browser [e.g., chrome, safari]
     - Version [e.g., 22]

     **Additional context**

     Add any other context about the problem here.
     ```

   - **Example Content for `documentation_template.md`:**
     ```markdown
     ## 📝 Documentation Update

     **What type of documentation is being updated?**

     - [ ] README
     - [ ] Wiki
     - [ ] API Docs
     - [ ] Other: _______

     **Describe the changes made**

     A clear and concise description of what changes were made to the documentation.

     **Additional context**

     Add any other context or screenshots about the documentation update here.
     ```

## **Setting Up Pull Request Templates**

1. **Create the Directory:**

   Ensure that the `.github/PULL_REQUEST_TEMPLATE/` directory exists in your repository. If it doesn't, create it using the following command:

   ```bash
   mkdir -p .github/PULL_REQUEST_TEMPLATE/
   ```

2. **Add Templates:**

   - **Single Template Approach:**

     If you prefer a single template for all pull requests, create a `pull_request_template.md` file inside the `.github/PULL_REQUEST_TEMPLATE/` directory and add the desired content.

   - **Multiple Templates Approach:**

     For multiple templates, create separate `.md` files with descriptive names (e.g., `feature_template.md`, `bugfix_template.md`) inside the `.github/PULL_REQUEST_TEMPLATE/` directory. Contributors will then be able to choose the appropriate template when creating a new pull request.

3. **GitHub Recognition:**

   GitHub automatically detects pull request templates placed in the `.github/PULL_REQUEST_TEMPLATE/` directory. When a contributor opens a new pull request, they will see an option to select from the available templates if multiple are present.

## **Best Practices for Pull Request Templates**

- **Clarity and Conciseness:**

  Ensure that templates are clear and concise, guiding contributors to provide all necessary information without being overly verbose.

- **Customization:**

  Tailor templates to fit the specific needs and workflows of your project. Include sections that are relevant and omit those that are not.

- **Consistency:**

  Maintain a consistent structure across different templates to make it easier for contributors to fill them out correctly.

- **Encourage Detailed Descriptions:**

  Prompt contributors to provide detailed explanations, which can help reviewers understand the changes and assess their impact effectively.

- **Automate Where Possible:**

  Use default values or placeholders to guide contributors on what information to provide, reducing the likelihood of missing details.

## **Additional Resources**

- **GitHub Documentation on PR Templates:**

  [Configuring pull request templates](https://docs.github.com/en/github/building-a-strong-community/using-pull-request-templates)

- **Example Repositories with PR Templates:**

  Reviewing how other repositories implement their PR templates can provide inspiration and best practices.

By setting up well-structured pull request templates, you streamline the contribution process, improve communication between contributors and maintainers, and enhance the overall quality of your project's codebase.

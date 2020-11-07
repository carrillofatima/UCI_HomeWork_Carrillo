--DATA ANALASYS
-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT EMP.emp_no, last_name, first_name, sex, salary
FROM employees AS EMP
JOIN salaries AS SAL ON
EMP.emp_no = SAL.emp_no;
SELECT * FROM employees; 
-- 2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name, last_name, hire_date 
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
SELECT deps.dept_no, dept_name, dm.emp_no, last_name, first_name
FROM departments AS deps
JOIN dept_manager AS dm 
ON deps.dept_no = dm.dept_no
JOIN employees AS emp 
ON emp.emp_no = dm.emp_no;

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT emp.emp_no, last_name, first_name, dept_name
FROM departments AS deps
JOIN dept_manager AS dm 
ON deps.dept_no = dm.dept_no
JOIN employees AS emp 
ON emp.emp_no = dm.emp_no;

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name, sex
FROM employees
WHERE first_name = 'Hercules' 
AND last_name LIKE 'B%';

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT emp.emp_no, last_name, first_name, deps.dept_name
FROM employees AS emp
FROM departments AS deps
JOIN dept_manager AS dm 
ON deps.dept_no = dm.dept_no
JOIN employees AS emp 
ON emp.emp_no = dm.emp_no;

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT emp.emp_no, emp.last_name, emp.first_name, deps.dept_name
FROM employees AS emp
JOIN dept_manager AS dm 
ON emp.emp_no = dm.emp_no
JOIN departments AS deps
ON deps.dept_no = dm.dept_no
WHERE deps.dept_name = 'Sales' OR 
deps.dept_name = 'Development';

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT COUNT(last_name), last_name
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;
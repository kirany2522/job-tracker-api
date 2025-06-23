const apiUrl = "https://job-tracker-api-3nff.onrender.com/api/jobs";

// POST: Add new job
document.getElementById("jobForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const company = document.getElementById("company").value;
  const role = document.getElementById("role").value;

  const response = await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ company, role })
  });

  const data = await response.json();
  alert(data.message);
  loadJobs();
});

// GET: Load all jobs
async function loadJobs() {
  const response = await fetch(apiUrl);
  const jobs = await response.json();
  const jobList = document.getElementById("jobList");
  jobList.innerHTML = "";

  jobs.forEach(job => {
    const li = document.createElement("li");
    li.textContent = `${job.company} - ${job.role}`;
    jobList.appendChild(li);
  });
}

// Load jobs on page load
loadJobs();

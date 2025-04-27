chrome.storage.session.get("selectedContent")
  .then(({ selectedContent }) => {
    document.getElementById("preview").innerText = selectedContent || "";
  });

async function classify(text) {
  const res = await fetch("http://localhost:5000/api/classify/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });
  return res.json();
}

async function submitCorrection(orig, corr) {
  await fetch("http://localhost:5000/api/submit-correction/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      original_text: orig,
      correction_text: corr,
      is_misinformation: true
    })
  });
}

document.getElementById("classifyBtn").onclick = async () => {
  const text = document.getElementById("preview").innerText;
  const { is_misinformation, score } = await classify(text);
  document.getElementById("result").innerText =
    is_misinformation
      ? `Misinformation (${(score * 100).toFixed(0)}%)`
      : `Looks OK (${(score * 100).toFixed(0)}%)`;
};

document.getElementById("result").innerHTML = `
  Misinformation: ${is_misinformation ? 
    `Yes (${(misinfo_score*100).toFixed(0)}%)` : 
    `No (${(misinfo_score*100).toFixed(0)}%)`}<br>
  Hate speech: ${is_hate_speech ? 
    `Yes (${(hate_score*100).toFixed(0)}%)` : 
    `No (${(hate_score*100).toFixed(0)}%)`}
`;

document.getElementById("flagBtn").onclick = () => {
  document.getElementById("correctionSection").classList.remove("hidden");
};

document.getElementById("submitCorrectionBtn").onclick = async () => {
  const orig = document.getElementById("preview").innerText;
  const corr = document.getElementById("correctionText").value;
  await submitCorrection(orig, corr);
  alert("Correction submitted! 🎉");
};

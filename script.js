import Html5QrcodeScanner from "html5-qrcode";
const html5QrCode = new Html5QrcodeScanner("result");
html5QrCode.render(onScanSuccess);


    function onScanSuccess(decodedText, decodedResult) {
        console.log(`Scan result: ${decodedText}`, decodedResult);
        const decodedText_sliced = decodedText.slice(0, 6);
        Papa.parse("./data_names.csv", {
          download: true,
          header: true,
          complete: (results) => {
            results.data.forEach((row) => {
              if (row[1] === decodedText_sliced) {
                const name = row[0];
                const patrouille = row[2];
                const p = document.createElement("p");
                const result = document.getElementById("result");
                const again = document.createElement("button");
                again.innerHTML = "Scan Again";
                result.innerHTML = p.innerHTML = `Welkom ${name} \n u ligt op kamping ${patrouille}`;
                result.appendChild(p);
                result.style.color = "white";
                result.style.display = "flex";
                result.style.flexDirection = "column";
                result.style.height = "100vh";
                result.style.fontSize = "2rem";
                result.style.textAlign = "center";
              }
            });
          },
        });
      }
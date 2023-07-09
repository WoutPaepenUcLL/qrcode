

//scanner on id camera


    
      // const onScanSuccess = async (decodedText, decodedResult) => {
      //   const response = await fetch('data_names.json');
      //   const data = await response.json();
      //   const decodedText_sliced = decodedText.slice(0, 36);
      //   const name = data.array.forEach(element => {
      //     if (element.id === decodedText_sliced) {
      //       return element.name;
      //     }
      //   });
      //   const patrouille = data.array.forEach(element => {
      //     if (element.id === decodedText_sliced) {
      //       return element.patrouille;
      //     }
      //   });
      //   const resultContainer = document.getElementById("result");
      //   resultContainer.innerHTML = `
      //     <div class="card">
      //       <div class="card-body">
      //         <h5 class="card-title">Naam : ${name}</h5>
      //         <h6 class="card-subtitle mb-2 text-muted">Patrouille : ${patrouille}</h6>
      //         <p class="card-text">ID : ${decodedText_sliced}</p>
      //       </div>
      //     </div>
      //   `;
      //   //stop the scanner
      //   html5QrCode.clear();
      //   document.getElementById("reader").remove();
      //   //scan again button
      //   const scanAgainButton = document.createElement("button");
      //   scanAgainButton.innerHTML = "Scan opnieuw";
      //   scanAgainButton.classList.add("btn", "btn-primary");
      //   scanAgainButton.addEventListener("click", () => {
      //     html5QrCode.start();
      //   }
      //   );
      // };
      
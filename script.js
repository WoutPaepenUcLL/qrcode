import Html5QrcodeScanner from "html5-qrcode";
const html5QrCode = new Html5QrcodeScanner("result");
html5QrCode.render(onScanSuccess);
function onScanSuccess(qrCodeMessage) {
    alert(`QR matched = ${qrCodeMessage}`);
    }
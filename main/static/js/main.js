document.getElementById("form").addEventListener("submit", async function(event) {
    event.preventDefault(); 
    const method = document.getElementById("method").value;
    const product = document.getElementById("product").value;
    const pk = document.getElementById("header").value;
    if(method=="GET"){
        const jsonData = await getJsonData(product, pk);
        document.getElementById("jsonData").innerText = JSON.stringify(jsonData, null, 4);
    }
    else if (method=="POST"){
        if (product=="Acara"){
            addAcara()
        }
        else if (product=="Divisi PI"){
            addDivisiPI()
        }
        else if (product=="PI"){
            addPI()
        }
        else if (product=="BPH"){
            addBPH()
        }
        else if (product=="Mentor"){
            addMentor()
        }
        else if (product=="Kelompok"){
            addKelompok()
        }
        else if (product=="Mentee"){
            addMentee()
        }
        else if (product=="Mentoring"){
            addMentoring()
        }
        else if (product=="Sponsor"){
            addSponsor()
        }
        else if (product=="Rapat"){
            addRapat()
        }
       
       
    }
    else if (method=="PUT"){
        if (product=="Acara"){
            putAcara(pk)
        }
        else if (product=="Mentor"){
            putMentor(pk)
        }
        else if (product=="Mentee"){
            putMentee(pk)
        }
        else if (product=="BPH"){
            putBPH(pk)
        }
        else if (product=="Sponsor"){
            putSponsor(pk)
        }
        else if (product=="Mentoring"){
            putMentoring(pk)
        }
        else if (product=="PI"){
            putPI(pk)
        }
        else if (product=="Add_Pembicara"){
            addPembicaraAcara(pk)
        }
        else if (product=="Absen_Mentoring"){
            hadirMentoring(pk)
        }
    }
    else if (method=="DELETE"){
        if (product=="Acara"){
            deleteAcara(pk)
        }
        else if (product=="Mentor"){
            deleteMentor(pk)
        }
        else if (product=="Mentee"){
            deleteMentee(pk)
        }
        else if (product=="BPH"){
            deleteBPH(pk)
        }
        else if (product=="Sponsor"){
            deleteSponsor(pk)
        }
        else if (product=="Mentoring"){
            deleteMentoring(pk)
        }
        else if (product=="Absen_Mentoring"){
            deleteHadirMentoring(pk)
        }
        else if (product=="Add_Pembicara"){
            deletePembicara(pk)
        }
        else if (product=="PI"){
            deletePI(pk)
        }
    }
   
});

function addAcara() {
    fetch("{% url 'main:acara' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan: ', error);
    });

    // 
    return false
}
function addMentee() {
    fetch("{% url 'main:mentee' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan: ', error);
    });

    // 
    return false
}
function addKelompok() {
    fetch("{% url 'main:kelompok' %}", {
        method: "POST",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2);  
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
}

function addMentoring() {
    fetch("{% url 'main:mentoring' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
}
function addRapat() {
    fetch("{% url 'main:rapat' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
}

function addSponsor() {
    fetch("{% url 'main:sponsor' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2);  
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
}


function addPI() {
    fetch("{% url 'main:pengurus_inti' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
}
function addBPH() {
    fetch("{% url 'main:bph' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });
    return false
}
function addMentor() {
    fetch("{% url 'main:mentor' %}", {
        method: "POST",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}

function hadirMentoring(header) {
    fetch(`api/hadir-mentoring/${header}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2);  
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}

function addPembicaraAcara(header) {
    fetch(`api/add-pembicara/${header}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function putAcara(acara) {
    fetch(`api/acara/${acara}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function putMentor(npm) {
    fetch(`api/mentor/${npm}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function putPI(header) {
    fetch(`api/pi/${header}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function putSponsor(header) {
    console.log("masuk")
    fetch(`api/sponsor/${header}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function putMentee(npm) {
    fetch(`api/mentee/${npm}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    document.getElementById("form").rest()
    return false
    
}

function putBPH(npm) {
    fetch(`api/bph/${npm}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function putMentoring(header) {
    fetch(`api/mentoring/${header}`, {
        method: "PUT",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deleteAcara(acara) {
    fetch(`api/acara/${acara}`, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deleteMentoring(acara) {
    fetch(`api/mentoring/${acara}`, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deleteSponsor(header) {
    fetch(`api/sponsor/${header}`, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deletePembicara(header) {
    fetch(`api/add-pembicara/${header}`, {
        method: "DELETE",
        body:document.getElementById("jsonInput").value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deletePI(header) {
    fetch(`api/pi/${header}`, {
        method:'DELETE'
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deleteMentee(npm) {
    fetch(`api/mentee/${npm}`, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deleteBPH(npm) {
    fetch(`api/bph/${npm}`, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    
    return false
    
}
function deleteMentor(npm) {
    fetch(`api/mentor/${npm}`, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    return false
    
}
function deleteHadirMentoring(header) {
    fetch(`api/hadir-mentoring/${header}`, {
        method: "DELETE",
        body: document.querySelector('#jsonInput').value
    }).then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(data => {
            throw new Error(data.error);
    });
        }
    }).then(data => {
        document.getElementById("jsonData").textContent = JSON.stringify(data, null, 2); 
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });

    return false
    
}




async function getJsonData(product,pk) {
    if (product=="Mentor"){
        return getMentors()
    }
    else if (product=="Acara"){
        return getAcara()
    }
    else if (product=="PI"){
        return getPI()
    }
    else if (product=="BPH"){
        return getBPH()
    }
    else if (product=="Panitia"){
        return getPanitia()
    }
    else if (product=="Kelompok"){
        return getKelompok()
    }
    else if (product=="Mentee"){
        return getMentees()
    }
    else if (product=="Sponsor"){
        return getSponsor()
    }
    else if (product=="Mentoring"){
        if(pk==""){
            return getMetoring()
        }
        const result= await getMetoring_kelompok(pk)
        return result
        
    }
    else if (product=="Rapat"){
        const result= await getRapat(pk)
        return result
        
    }

}
async function getMentors() { return fetch(`api/mentor/`).then((res) => res.json()) }
async function getMentees() { return fetch(`api/mentee/`).then((res) => res.json()) }
async function getAcara() { return fetch(`api/acara/`).then((res) => res.json()) }
async function getPI() { return fetch(`api/pi/`).then((res) => res.json()) }
async function getBPH() { return fetch(`api/bph/`).then((res) => res.json()) }
async function getPanitia() { return fetch(`api/panitia/`).then((res) => res.json()) }
async function getKelompok() { return fetch(`api/kelompok/`).then((res) => res.json()) }
async function getSponsor() { return fetch(`api/sponsor/`).then((res) => res.json()) }
async function getMetoring() { return fetch(`api/mentoring/`).then((res) => res.json()) }
async function getMetoring_kelompok(kelompok) {
    return fetch(`api/mentoring/${kelompok}`, {
        method: "GET",
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Gagal mengambil data');
        }
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });
    
}
async function getHadirMentoring(header) {
    return fetch(`api/hadir-mentoring/${header}`, {
        method: "GET",
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Gagal mengambil data');
        }
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });
    
}
async function getRapat(divisi) {
    return fetch(`api/rapat/${divisi}`, {
        method: "GET",
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Gagal mengambil data');
        }
    }).catch(error => {
        console.error('Terjadi kesalahan:', error);
    });
   
}
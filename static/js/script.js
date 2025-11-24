
function openAddModal() {
document.getElementById("addModal").style.display = "block";}

function closeAdd() {  document.getElementById("addModal").style.display = "none";}

 function openUpdateModal(id, name, phone, email, address, role) {
    document.getElementById("u_id").value = id;
    document.getElementById("u_name").value = name;
    document.getElementById("u_phone").value = phone;
    document.getElementById("u_email").value = email;
    document.getElementById("u_address").value = address;
    document.getElementById("updateModal").style.display = "block"; }

function closeUpdate() {
    document.getElementById("updateModal").style.display = "none";}

    // Flask update route 

document.getElementById("updateForm").onsubmit = function() {
        let id = document.getElementById("u_id").value;
        this.action = "/update/" + id;
    };
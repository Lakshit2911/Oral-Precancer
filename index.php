<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BioDB</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css"
        integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
</head>
<?php
session_start();
?>
<body class="d-flex text-center text-white bg-dark">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
        <header class="mb-auto">
            <div>
                <h3 class="float-md-left mb-0">Oral Pre Cancer Database</h3>
                <nav class="nav nav-masthead justify-content-center float-md-right">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                    <a class="nav-link" href="#">Know More</a>
                    <?php if(isset($_SESSION['User_Username']) || isset($_SESSION['Username'])) ?>
                    <!-- <a class="nav-link" href="#">Logout</a> -->
                        <a class="nav-link" href="database/loginPage.php">Login</a>
                        <a class="nav-link" href="Users/register.php">Register</a>

                </nav>
            </div>
        </header>
        <main class="px-3">
            <p class="lead"> <h2>Welcome to Oral Pre Cancer Database</h2> <br>
               <h5>Add a data to help world fight Cancer!</h5></p>
            <a href="database/showDB.php" class="btn btn-lg btn-secondary font-weight-bold border-white bg-white">See Database</a>
        </main>

        <footer class="mt-auto text-white-50">
            <p>&copy; 2022  </p>
        </footer>


    </div>


    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js"
        integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/"
        crossorigin="anonymous"></script>
</body>

</html>
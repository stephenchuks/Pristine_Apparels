<template>
  <div class="about">
    <div class="about-content">
      <h2>Welcome to Pristine Apparels</h2>
      <br />
      <p>
        Our objective is to provide you with an unparalleled shopping experience, tailored to your unique needs and preferences. Our website is designed to be user-friendly, informative, and easy to navigate, and our team of experienced professionals is dedicated to delivering excellent customer service. We are always available to answer any questions, address concerns, and provide assistance whenever needed.
      </p>
      <br />
      <br />
      <p>
        At Pristine Apparels, we take pride in offering top-quality products at reasonable prices, sourcing from reputable suppliers to ensure the highest quality. We continually update our inventory with new and exciting products, so make sure to check back regularly. We appreciate you choosing AjeboMart and we are excited to serve you and offer an exceptional shopping experience.
      </p>
      <p>
        If you have any inquiries or feedback, please don't hesitate to contact us.
      </p>
    </div>
    <div class="social-links">
      <h3>Connect with us:</h3>
      <ul>
        <li><a href="https://www.linkedin.com/in/chuks-humphrey-stephen-614907165/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a></li>
        <li><a href="https://github.com/stephenchuks" target="_blank"><i class="fab fa-github"></i> GitHub</a></li>
        <li><a href="mailto:stephenchumphrey@yahoo.com"><i class="fas fa-envelope"></i> Email</a></li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.about {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 20px;
  background-color: #f2f2f2;
}

.about-content {
  text-align: center;
  margin-bottom: 40px;
}

.about-content h2 {
  font-size: 30px;
  font-weight: bold;
  color: #333;
}

.about-content p {
  font-size: 18px;
  line-height: 1.5;
  color: #666;
}

.social-links {
  text-align: center;
  margin-bottom: 20px;
}

.social-links h3 {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
}

.social-links ul {
  list-style: none;
  padding: 0;
}

.social-links ul li {
  display: inline-block;
  margin-right: 10px;
}

.social-links ul li:last-child {
  margin-right: 0;
}

.social-links ul li a {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: border-bottom-color 0.3s ease;
}

.social-links ul li a:hover {
  border-bottom-color: #333;
}
</style>

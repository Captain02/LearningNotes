package com.micro.provider.microprovider8001;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableEurekaClient
public class MicroProvider8001Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroProvider8001Application.class, args);
	}

}

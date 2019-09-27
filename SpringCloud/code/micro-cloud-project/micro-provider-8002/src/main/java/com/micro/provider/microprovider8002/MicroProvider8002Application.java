package com.micro.provider.microprovider8002;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableEurekaClient
public class MicroProvider8002Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroProvider8002Application.class, args);
	}

}

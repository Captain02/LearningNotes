package com.micro.consumer.config.microconsumerconfig9003.dept.controller;

import com.entity.Dept;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
public class DeptController {

    private static final String REST_URL_PREFIX2 = "http://MICRO-PROVIDER";
    private static final String REST_URL_PREFIX = "http://MICRO-ZUUL-GATEWAY/micro/mydept";

    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/getlist")
    public List<Dept> getdept() {
        return restTemplate.getForObject(REST_URL_PREFIX + "/getlist", List.class);
    }

    @GetMapping("/getlist2")
    public List<Dept> getdept2() {
        return restTemplate.getForObject(REST_URL_PREFIX2 + "/getlist", List.class);
    }
}

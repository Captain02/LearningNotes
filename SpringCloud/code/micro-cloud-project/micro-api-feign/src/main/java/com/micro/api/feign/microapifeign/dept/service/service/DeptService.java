package com.micro.api.feign.microapifeign.dept.service.service;

import com.micro.api.feign.microapifeign.dept.service.bean.Dept;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.List;


@FeignClient(value = "MICRO-PROVIDER", fallbackFactory = DeptClientServiceFallbackFactory.class)
public interface DeptService {

    //服务中方法的映射路径,去注册中心寻找其他的相同映射的服务，实现服务在均衡
    @RequestMapping(value = "/getlist", method = RequestMethod.GET)
    public List<Dept> getList();
}

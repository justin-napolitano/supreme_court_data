using DataFrames
using CSV
import JSON

function get_files(directory)
    file_name = String[]
    file_path = String[]

    working_path = joinpath(pwd(), directory)
    # context management.  Cd and then go back to the orignal pwd
    cd(working_path) do 
        #print("Current directory: ", working_path)
        foreach(readdir()) do f
            path = joinpath(working_path, f)
            push!(file_name,f)
            push!(file_path, path)
            #dump(stat(f.desc)) # you can customize what you want to print
        end
    end
    #println('\n', pwd())
    #display(file_paths)
    file_name = sort_array(file_name)
    file_path = sort_array(file_path)
    df = DataFrame(File = file_name, Path = file_path)
    return df

end



function sort_array(array)
    
    return sort(array; alg=MergeSort)

end



function df_to_file(df,outpath)
    CSV.write(outpath, df)
    return outpath

end


function read_json(json_path)
    dict = Dict()
    dict = JSON.parsefile(json_path)
    
    return dict

end


function main()
    
    # outpath fo the current file
    inpath = joinpath(pwd(),"case_files.csv")

    #Create a df from the case_files.csv file
    master_df = DataFrame(CSV.File(inpath))

    test = master_df[1,"Path"]
    dict = read_json(test)

    for i in dict
        println(i)
    end

    
    #for row in Tables.namedtupleiterator(master_df)
    #    oyez_dict= read_json(row.Path)
    #    loc_dict = read_json(row.Path_1)
        #oyez_dict("PDF" => loc_dict.pdf)
        #key = keys(loc_dict)
    #    display(loc_dict)
    #end
    #json = read_json(master_df.Path[0])

    #Write to file
    #outpath = df_to_file(master_df,outpath)
    

end

main()

